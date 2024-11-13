import shutil
import os

def deploy():
    deploy_dir = "C:\\deploy"
    if not os.path.exists(deploy_dir):
        os.makedirs(deploy_dir)
    shutil.copyfile("app.py", os.path.join(deploy_dir, "app.py"))
    print("Deployment complete!")

if __name__ == "__main__":
    deploy()
