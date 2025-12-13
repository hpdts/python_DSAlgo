import json
import os

def getF2PandP2P(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    F2P = data["fail_to_pass"]
    cleaned_tests_f2p = {test.split("(", 1)[0] for test in F2P}

    P2P = data["pass_to_pass"]
    cleaned_tests_p2p = {test.split("(", 1)[0] for test in P2P}

    return cleaned_tests_f2p,cleaned_tests_p2p

def f2p_p2p_not_inlog(cleaned_tests, log_file):
    with open(log_file, "r") as f:
        log_data = f.read()
        missing = [test for test in sorted(cleaned_tests) if test not in log_data]
        print(f"Missing count in {log_file}: {len(missing)}")

        for test in sorted(cleaned_tests):
            if test not in log_data:
                print(test)

def f2p_present_inlog(cleaned_tests, log_file):
    with open(log_file, "r") as f:
        log_data = f.read()
        present = [
            test for test in sorted(cleaned_tests)
            if test in log_data and f"{test} FAILED" not in log_data
        ]
        print(f"Present count in {log_file}: {len(present)}")
        for test in sorted(cleaned_tests):
            if test in log_data:
                pattern = f"{test} FAILED"
                if pattern not in log_data:
                    print(test)

def f2p_p2p_present_inreportnotinpost(cleaned_tests, report_json, post_file):
    with open(post_file, "r") as f:
        post_log_data = f.read()

    with open(report_json, "r") as f:
        report_log_data = f.read()
        for test in sorted(cleaned_tests):
            if test in report_log_data and test not in post_log_data:
                print(test)

def find_log_file(folder: str, suffix: str) -> str | None:
    for fname in os.listdir(folder):
        if suffix in fname and fname.endswith(".log"):
            return os.path.join(folder, fname)
    return None

def find_json_file(folder: str, suffix:str) -> str | None:
    for fname in os.listdir(folder):
        if fname.endswith(f"{suffix}.json"):
            return os.path.join(folder, fname)
    return None

def find_report_file(folder: str) -> str | None:
    for fname in os.listdir(folder):
        if fname.endswith(".json"):
            return os.path.join(folder, fname)
    return None

task_number = "159266"
folder_path = f"/Users/franciscohernandez/Documents/Fco2024-25/turing/c#/tasks/{task_number}/"
#folder_path = f"/Users/franciscohernandez/Documents/Fco2024-25/turing/python/{task_number}/"
json_file = find_json_file(folder_path, "_p2p")
after_file = find_log_file(folder_path, "_after")
before_file = find_log_file(folder_path, "_before")
base_file = find_log_file(folder_path, "_base")
print(f"Using found json file: {json_file}")
print(f"Using found before file log: {before_file}")
print(f"Using found base file log: {base_file}")
print(f"Using found after file log: {after_file}")

cleaned_tests_f2p, cleaned_tests_p2p = getF2PandP2P(json_file)
#print(f"Unique cleaned F2P test count: {cleaned_tests_f2p}")
# print(f"Unique cleaned P2P test count: {cleaned_tests_p2p}")
print("Check P2P and F2P tests in after log")
print("At least one failed or missing after test in log is present in F2P:")
f2p_p2p_not_inlog(cleaned_tests_f2p, after_file)
print("At least one failed or missing after test in log is present in P2P:")
f2p_p2p_not_inlog(cleaned_tests_p2p, after_file)

print("At least one F2P test is present and successful in before log")
f2p_present_inlog(cleaned_tests_f2p, before_file)

print("At least one P2P, that is missing in base")
f2p_p2p_not_inlog(cleaned_tests_p2p, base_file)

print("9: If report.json and post_agent_log are not empty: at least one F2P / P2P in report.json success/failure status is not matching post_agent_log")
report_json = find_json_file(folder_path, "report")
post_file = find_log_file(folder_path, "_post_agent_patch")
print(f"Using found report json file: {report_json}")
print(f"Using found post file log: {post_file}")
f2p_p2p_present_inreportnotinpost(cleaned_tests_f2p, report_json, post_file)
f2p_p2p_present_inreportnotinpost(cleaned_tests_p2p, report_json, post_file)

print("All good")

exit()