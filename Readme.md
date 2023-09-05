Dataset download from: http://openkg.cn/dataset/yidu-s4k


# experiment of fine-tune openai davinci model to solve NER task

# installation
pip install --upgrade openai

# 配置環境變數
export OPENAI_API_KEY=xxx

# CLI data preparation tool (重新規範訓練集的格式)
openai tools fine_tunes.prepare_data -f entities_.json

# create a fine-tuned model
openai api fine_tunes.create -t entities_prepared.jsonl -m davinci


openai api completions.create -m davinci:ft-personal-2023-08-25-15-33-13 -p <YOUR_PROMPT>