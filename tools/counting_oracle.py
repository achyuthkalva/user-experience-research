"""Deterministic oracle for synthetic participant/task fixtures only.

This validates expected test counts. It does not code qualitative data, run a
model, infer participant identities, or decide which real evidence is valid.
"""
from __future__ import annotations
from typing import Any


def summarise_task(records: list[dict[str, Any]], study: str, task: str) -> dict[str, Any]:
    participants: dict[str, dict[str, Any]] = {}
    notes: dict[str, dict[str, Any]] = {}
    allowed = {None, "unaided_success", "unaided_failure"}
    for record in records:
        if record.get("study_id") != study or record.get("task_id") != task:
            continue
        for field in ("participant_id", "note_id"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Missing {field}")
        if type(record.get("exposed")) is not bool:
            raise ValueError("Exposure must be explicit true/false in this fixture")
        if record.get("outcome") not in allowed:
            raise ValueError("Unknown outcome value")
        if type(record.get("assisted_completion", False)) is not bool:
            raise ValueError("Assistance must be boolean")
        if not record["exposed"] and (record.get("outcome") is not None or record.get("assisted_completion", False)):
            raise ValueError("Unexposed participant cannot have a task outcome")
        nid, pid = record["note_id"], record["participant_id"]
        if nid in notes:
            if notes[nid] != record:
                raise ValueError("Conflicting records use the same note ID")
            continue
        notes[nid] = dict(record)
        state = {"exposed": record["exposed"], "outcome": record.get("outcome"),
                 "assisted_completion": record.get("assisted_completion", False)}
        if pid in participants:
            previous = participants[pid]
            if previous["exposed"] != state["exposed"] or previous["outcome"] != state["outcome"]:
                raise ValueError("Conflicting participant outcomes require human resolution")
            previous["assisted_completion"] |= state["assisted_completion"]
        else:
            participants[pid] = state
    known = sorted(p for p, s in participants.items() if s["exposed"] and s["outcome"] is not None)
    failed = sorted(p for p in known if participants[p]["outcome"] == "unaided_failure")
    missing = sorted(p for p, s in participants.items() if s["exposed"] and s["outcome"] is None)
    unexposed = sorted(p for p, s in participants.items() if not s["exposed"])
    assisted = sorted(p for p, s in participants.items() if s["assisted_completion"])
    return {"study_id": study, "task_id": task, "participants": sorted(participants),
            "failure_count": len(failed), "known_outcome_denominator": len(known),
            "failed_unaided": failed, "known_outcomes": known, "missing_outcomes": missing,
            "unexposed": unexposed, "assisted_completion": assisted}
