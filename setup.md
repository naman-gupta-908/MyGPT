Install python 3.13 and anaconda

Create a folder "MyGPT"

Open Anaconda prompt and then run the following commands:

1: Create a virtualenv:

python -m venv cuda

2: Activate that virtualenv

cuda\Scripts\activate

3: Install the required libraries

pip3 install matplotlib numpy ipykernel jupyter

pip3 install torch --index-url https://download.pytorch.org/whl/cu128

4: Setup the virtualenv created above as the jupyter kernel with name "MyGPT"

python -m ipykernel install --user --name=cuda --display-name "MyGPT"

5: Start the jupyter notebook

jupyter notebook

