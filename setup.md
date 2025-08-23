Install python 3.10 anaconda

Create a folder "MyGPT"

Open Anaconda prompt and then run the following commands:

1: Create a virtualenv:

conda create -n torch110_py310 python=3.10 -y

2: Activate that virtualenv

activate torch110_py310 

3: Install the required libraries

pip install torch==1.11.0+cu115 -f https://download.pytorch.org/whl/torch_stable.html

pip3 install matplotlib numpy ipykernel jupyter

4: Setup the virtualenv created above as the jupyter kernel with name "MyGPTCuda"

python -m ipykernel install --user --name=torch110_py310 --display-name "MyGPTCuda"

5: Start the jupyter notebook

jupyter notebook

