import launch

packages = [
    "huggingface_hub>=0.20.0",
    "requests"
]

for pkg in packages:
    if not launch.is_installed(pkg.split(">=")[0]):
        launch.run_pip(
            f"install {pkg}",
            pkg
        )
