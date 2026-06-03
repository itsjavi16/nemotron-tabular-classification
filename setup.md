# Setup Guide — Nemotron Classification Project

## Hardware Requirements

| Device | GPU | VRAM | RAM | Purpose |
|---|---|---|---|---|
| Local laptop | RTX 4060 Laptop | 8 GB | 32 GB | Nemotron Nano 4B experiments |
| FDS workstation | RTX 5000 Ada | 32 GB | 128 GB | Nemotron Nano 30B experiments |

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/itsjavi16/nemotron-classification.git
cd nemotron-classification
```

---

## Step 2 — Install Miniconda (if not already installed)

Download from: https://docs.anaconda.com/miniconda/

- Windows: run the `.exe` installer, check **Add to PATH**
- Restart your terminal after installing

---

## Step 3 — Create the Conda Environment

### Local laptop (Nano 4B experiments)

```bash
conda create -n nemotron-local python=3.11 -y
conda activate nemotron-local
pip install -r requirements.txt
python -m ipykernel install --user --name nemotron-local --display-name "Nemotron Local (4B)"
```

### FDS workstation (Nano 30B experiments)

```bash
conda create -n nemotron-fds python=3.11 -y
conda activate nemotron-fds
pip install -r requirements.txt
python -m ipykernel install --user --name nemotron-fds --display-name "Nemotron FDS (30B)"
```

---

## Step 4 — Install Ollama

Download from: https://ollama.com

### Pull the Nemotron models

**Local laptop (Nano 4B):**
```bash
ollama pull nemotron-3-nano:4b
```

**FDS workstation (Nano 30B):**
```bash
ollama pull nemotron-3-nano:30b-a3b-q4_K_M
```

Make sure Ollama is running before launching any notebooks:
```bash
ollama serve
```

---

## Step 5 — Download the Dataset

The dataset downloads automatically on first run of `week1_baselines.ipynb`.

```python
from datasets import load_dataset
ds = load_dataset("nvidia/Nemotron-Personas-USA")
```

> **Note:** First download is ~2.7 GB. Make sure you are on a good internet connection.

---

## Step 6 — Open VSCode and Select Kernel

1. Open the repo folder in VSCode
2. Open any `.ipynb` notebook
3. Click the kernel selector (top-right corner)
4. Choose **Nemotron Local (4B)** or **Nemotron FDS (30B)**

---

## Project Structure

```
nemotron-classification/
├── data/
│   └── personas_sample_500.csv    # 500-row LLM test sample (gitignored)
├── models/                        # Model files (gitignored)
├── notebooks/
│   ├── week1_baselines.ipynb      # RF and XGBoost baselines
│   ├── week2_prompts.ipynb        # Prompt engineering pipeline
│   ├── week3_nano4b_results.ipynb # Nano 4B experiments + K-Means
│   ├── week4_nano30b_results.ipynb# Nano 30B experiments (FDS)
│   └── week5_analysis.ipynb       # Error analysis + fine-tuning
├── src/
│   ├── serialize.py               # Row → natural language
│   ├── prompts.py                 # Prompt builders
│   ├── parse_response.py          # Extract label from response
│   ├── infer_local.py             # Ollama inference (local)
│   ├── infer_fds.py               # Ollama inference (FDS)
│   └── evaluate.py                # Metrics computation
├── results/
│   └── metrics.csv                # All experiment results
├── requirements.txt               # Python dependencies
├── SETUP.md                       # This file
└── README.md                      # Project overview
```

---

## Running Order

Run notebooks in this order:

1. `week1_baselines.ipynb` — establishes RF and XGBoost baselines
2. `week2_prompts.ipynb` — builds and tests the prompt pipeline
3. `week3_nano4b_results.ipynb` — runs Nano 4B experiments locally
4. `week4_nano30b_results.ipynb` — runs Nano 30B experiments on FDS
5. `week5_analysis.ipynb` — error analysis and fine-tuning

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `conda: command not found` | Open Anaconda Prompt instead of regular terminal |
| `ollama: command not found` | Install Ollama from ollama.com and restart terminal |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` in the correct conda env |
| Kernel not showing in VSCode | Run `python -m ipykernel install --user --name nemotron-local` |
| Dataset download fails | Check internet connection — needs ~2.7 GB download |
| Ollama connection refused | Run `ollama serve` in a separate terminal |
| CUDA out of memory | Reduce batch size or use a smaller quantization |