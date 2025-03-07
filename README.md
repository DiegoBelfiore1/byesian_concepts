<h1 align="center"> 🧑🏻‍💻 BC-LLM - Reproduction </h1>
<p align="center"> <b>Bayesian Concept Bottleneck Models with LLM Priors by</b>  <a href="https://arxiv.org/abs/2410.15555">Feng et al. 2024</a>. 
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-mit-green.svg">
  <img src="https://img.shields.io/badge/python-3.7+-blue">
</p>  

![](./overview.png)

> This is the work done on a model built by Feng et al. The model consists in the sequent structure.



## Reproducing experiments
All experiments are managed using `scons` and `nestly`.
If you want to run a single experiment, specify the experiment's folder name, e.g. `scons exp_mimic`.

**LLM Api**

To use the either the OpenAI models or Hugging Face models through the API add a .env file in the root folder of this directory

```bash
llm-vi $ touch .env
```

Add your token for Open AI and/or Hugging face
```bash
llm-vi $ echo "OPENAI_ACCESS_TOKEN=<YOUR TOKEN>" >> .env
llm-vi $ echo "HF_ACCESS_TOKEN=<YOUR TOKEN>" >> .env
```


### Citation
If you find our paper and code useful, please cite us:
```r
@misc{feng2024bcllm,
      title={Bayesian Concept Bottleneck Models with LLM Priors}, 
      author={Jean Feng and Avni Kothari and Luke Zier and Chandan Singh and Yan Shuo Tan},
      year={2024},
      eprint={2410.15555},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2410.15555}, 
}
```