import unittest

import requests

HOST = "localhost:8000"


class EditTaskCase(unittest.TestCase):
    test_data = {"title": "task1",
                 "description": "new task 1",
                 "due_date": "2026-07-26T13:33:03.969Z"
                 }
    task_msg = requests.post(HOST + "/test/add", data=test_data).json()['msg']

    def test_success(self):
        task_id = int(self.task_msg.split()[1].replace("#", ""))
        edit_data = {"task_id": task_id,
                     "change_field": "description",
                     "content": "new description for task"
                     }
        self.assertEqual(requests.post(HOST + "/test/edit", data=edit_data).json(), {'msg': f"task #{task_id} changed"})

    def test_fail(self):
        edit_data = {"task_id": -1,
                     "change_field": "description",
                     "content": "new description for task"
                     }
        self.assertEqual(requests.post(HOST + "/test/edit", data=edit_data).json(),
                         {"msg": "no task with the following id"})


if __name__ == '__main__':
    unittest.main()