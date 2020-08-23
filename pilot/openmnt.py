import opennmt

config = {
    "model_dir": "../third_party/opennmt/",
    "data": {
        "source_vocabulary": "../third_party/opennmt/assets/korean-english-park.train/korean-english-park.train.en.vocab",
        "target_vocabulary": "../third_party/opennmt/assets/korean-english-park.train/korean-english-park.train.ko.vocab"
    }
}

model = opennmt.models.TransformerBase()
runner = opennmt.Runner(model, config, auto_config=True)
runner.infer("../README.md")