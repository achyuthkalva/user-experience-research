import copy
import unittest
from tools.counting_oracle import summarise_task


def fixture():
    rows = []
    for i in range(1, 9):
        rows.append({"study_id": "DEMO-01", "task_id": "FIND", "note_id": f"E{i:02d}",
                     "participant_id": f"P{i:02d}", "exposed": i < 8,
                     "outcome": "unaided_failure" if i <= 4 else "unaided_success" if i <= 6 else None,
                     "assisted_completion": i == 2})
    return rows


class CountingTests(unittest.TestCase):
    def run_fixture(self, rows):
        return summarise_task(rows, "DEMO-01", "FIND")

    def test_correct_numerator_and_denominator(self):
        r = self.run_fixture(fixture())
        self.assertEqual((r["failure_count"], r["known_outcome_denominator"]), (4, 6))

    def test_missing_and_unexposed_remain_distinct(self):
        r = self.run_fixture(fixture())
        self.assertEqual(r["missing_outcomes"], ["P07"])
        self.assertEqual(r["unexposed"], ["P08"])

    def test_assistance_does_not_erase_failure(self):
        r = self.run_fixture(fixture())
        self.assertEqual(r["assisted_completion"], ["P02"])
        self.assertIn("P02", r["failed_unaided"])

    def test_duplicate_note_not_counted_twice(self):
        rows = fixture()
        rows.append(copy.deepcopy(rows[0]))
        self.assertEqual(self.run_fixture(rows), self.run_fixture(fixture()))

    def test_repeated_participant_not_counted_twice(self):
        rows = fixture()
        x = copy.deepcopy(rows[0]); x["note_id"] = "E09"; rows.append(x)
        self.assertEqual(self.run_fixture(rows), self.run_fixture(fixture()))

    def test_conflicting_note_id_rejected(self):
        rows = fixture(); x = copy.deepcopy(rows[0]); x["outcome"] = "unaided_success"; rows.append(x)
        with self.assertRaises(ValueError): self.run_fixture(rows)

    def test_conflicting_participant_outcomes_rejected(self):
        rows = fixture(); x = copy.deepcopy(rows[0]); x.update(note_id="E09", outcome="unaided_success"); rows.append(x)
        with self.assertRaises(ValueError): self.run_fixture(rows)

    def test_other_studies_and_tasks_not_pooled(self):
        rows = fixture(); x = copy.deepcopy(rows[0]); x["study_id"] = "OTHER"; rows.append(x)
        y = copy.deepcopy(rows[0]); y["task_id"] = "OTHER"; rows.append(y)
        self.assertEqual(self.run_fixture(rows), self.run_fixture(fixture()))

    def test_missing_identity_rejected(self):
        rows = fixture(); rows[0]["participant_id"] = ""
        with self.assertRaises(ValueError): self.run_fixture(rows)

    def test_known_outcome_without_exposure_rejected(self):
        rows = fixture(); rows[0]["exposed"] = False
        with self.assertRaises(ValueError): self.run_fixture(rows)

    def test_all_unknown_has_zero_known_denominator(self):
        rows = fixture()
        for r in rows: r["outcome"] = None
        self.assertEqual(self.run_fixture(rows)["known_outcome_denominator"], 0)

    def test_empty_data_produces_no_invented_people(self):
        r = self.run_fixture([])
        self.assertEqual(r["participants"], [])
        self.assertEqual(r["failure_count"], 0)

    def test_invalid_outcome_rejected(self):
        rows = fixture(); rows[0]["outcome"] = "probably failed"
        with self.assertRaises(ValueError): self.run_fixture(rows)

    def test_non_boolean_exposure_rejected(self):
        rows = fixture(); rows[0]["exposed"] = "yes"
        with self.assertRaises(ValueError): self.run_fixture(rows)
