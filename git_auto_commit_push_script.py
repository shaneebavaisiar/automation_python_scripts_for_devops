import subprocess  # It is used to run git commands using python

def git_commit_push(commit_msg):
    subprocess.run(["git","add","."],check=True)
    subprocess.run(["git","commit","-m",commit_msg],check=True)
    subprocess.run(["git","push","origin","feature"],check=True)
    print("chages pushed to remote repository !!!")

git_commit_push("add first automation script")
