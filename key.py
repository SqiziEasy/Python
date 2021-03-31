objects = [{
    "math": [
    {
        "task_number": [
        {
            "3": [
            {
                "variants_of_task": [
                {
                    "difficult": "1",
                    "question": "текст задания",
                    "answer": "122"
                }]
            }]
        }]
    }]
}]

print(objects[0]["math"][0]["task_number"][0]["3"][0]["variants_of_task"][0]["answer"])
#["task_number"]["3"]["variants_of_task"])