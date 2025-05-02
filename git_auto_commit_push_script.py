import subprocess  # Here we used to run git commands using python
"""In Python, the subprocess module is used to run external programs (or commands) from 
within your Python script.
It allows your Python code to interact with the system shell and other programs—just 
like if you were typing commands in a terminal or command prompt."""
def git_commit_push(branch_name,commit_msg):
    subprocess.run(["git","branch",branch_name],check=True)
    subprocess.run(["git","checkout",branch_name],check=True)
    print(f"you checked out into {branch_name}")
    subprocess.run(["git","add","."],check=True)
    subprocess.run(["git","commit","-m",commit_msg],check=True)
    subprocess.run(["git","push","origin","feature"],check=True)
    print("chages pushed to remote repository !!!")

git_commit_push("feature1","add updated automation script")
