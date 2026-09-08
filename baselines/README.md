# Baseline runners

Each Python file is one independently runnable VideoPhy-2 baseline:

- `direct_vlm.py`: caption + fixed uniform frames -> direct PC score.
- `rubric_vlm.py`: caption + caption-specific rubric + fixed uniform frames -> item decisions -> deterministic SA/PC scores.
- `videophy2_autoeval.py`: official released VideoPhy-2-AutoEval checkpoint -> PC score.

Preflight without making API/model calls:

```bash
python baselines/direct_vlm.py --check-only --n 20
python baselines/rubric_vlm.py --check-only --n 20
python baselines/videophy2_autoeval.py --check-only --n 20
```

Example smoke runs:

```bash
python baselines/direct_vlm.py --n 20 --limit 2
python baselines/rubric_vlm.py --n 20 --limit 2
python baselines/videophy2_autoeval.py --n 20 --limit 2 --device cuda
```

The two API-backed baselines use `configs/default.yaml` and the environment
variable named by `llm.api_key_env`. AutoEval uses the shared local checkpoint
under `/home/jovyan/models/videophy_2_auto`. Its official runtime requires a CUDA PyTorch build,
`decord`, `sentencepiece`, and the released `mplug_owl_video` sources saved with
the checkpoint. The upstream code was written for `transformers==4.28.1`; use a
separate environment for AutoEval rather than downgrading the main project.

Every runner writes append-only JSONL results and a `.summary.json` containing
Pearson, Spearman, Kendall, MAE, RMSE, exact accuracy, and within-one accuracy.
