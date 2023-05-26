import streamlit as st
import subprocess

def install_packages():
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

def run_app():
    subprocess.call(['streamlit', 'run', 'app.py'])

def main():
    install_packages()
    run_app()

if __name__ == '__main__':
    main()
