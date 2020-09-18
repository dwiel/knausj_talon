from talon import Context, Module, actions, grammar

# Add single words here if Talon recognizes them, but they need to have their
# capitalization adjusted.
capitalize = [
    "I",
    "I'm",
    "I've",
    "I'll",
    "I'd",
    "Monday",
    "Mondays",
    "Tuesday",
    "Tuesdays",
    "Wednesday",
    "Wednesdays",
    "Thursday",
    "Thursdays",
    "Friday",
    "Fridays",
    "Saturday",
    "Saturdays",
    "Sunday",
    "Sundays",
    "January",
    "February",
    # March omitted because it's a regular word too
    "April",
    # May omitted because it's a regular word too
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Add words (or phrases you want treated as words) here if Talon doesn't
# recognize them at all.
word_map = {
    # For example:
    # "color": "colour",
}
word_map.update({x.lower(): x for x in capitalize})

simple_vocabulary = [
    "nmap",
    "admin",
    "Cisco",
    "Citrix",
    "VPN",
    "DNS",
    "minecraft",
    "unhashable",
    "pycharm",
    "optuna",
    "streamlit",
    "postgres",
    "terran robotics",
    "mavlink",
    "yaw",
    "DJI",
    "DGI",
    "attitude quaternion",
    "quaternion",
    "acceleration",
    "accelerometer",
    "accelerometers",
    "env",
    "peek wrapper",
    "pitch deck",
    "PWD",
    "Wget",
    "SSH",
    "make run",
    "make shell",
    "make clean",
    "smartnav",
    "pip",
    "pip install",
    "ipython",
    "python",
    "iter",
    "NP",
    "yield",
    "python3",
    "conda",
    "functools",
    "matplotlib",
    "redis",
    "args",
    "dict",
    "traceback",
    "refactor",
    "contrib",
    "yaml",
    "yamel",
    "namespace",
    "namespaced",
    "pull request",
    "rebase",
    "rebased",
    "mergeable",
    "DQN",
    "N step replay buffer",
    "cart pole",
    "RLkit",
    "IMU",
    "quat",
    "autonomously",
    "much reese",
    "LSTM",
    "RNN",
    "KNN",
    "GRU",
    "GPU",
    "SGD",
    "VAE",
    "beta VAE",
    "word2vec",
    "op graph",
    "initializer",
    "keras",
    "tensorflow",
    "pytorch",
    "matmul",
    "frontends",
    "expand dims",
    "gan",
    "NG",
    "minibatch",
    "affine",
    "affine layer",
    "affine embedding",
    "linear layer",
    "elementwise",
    "argmax",
    "encode",
    "onehot",
    "multihot",
    "embeddings",
    "end to end",
    "unordered axes",
    "convolution",
    "convolutional",
    "conv",
    "conv net",
    "hyper parameter",
    "epsilon",
    "start epsilon",
    "end epsilon",
    "model end",
    "discretized",
    "decay",
    "embedder",
    "docker",
    "dockerfile",
    "docker compose",
    "folsom",
    "folsom lab",
    "ncloud",
    "SGI",
    "IPFS",
    "ethereum",
    "brew install",
    "voicecode",
    "IU",
    "fiaz",
    "yinyin",
    "evren",
]

mapping_vocabulary = {
    "i": "I",
    "i'm": "I'm",
    "i've": "I've",
    "i'll": "I'll",
    "i'd": "I'd",
    "open A I": "openai",
    "opening I": "openai",
    "talent": "talon",
    "minards": "menards",
    "hi": "high",
    "rose": "rows",
    "wi fi": "wifi",
    "2d d": "2d",
    "3d d": "3d",
    ".": "dot",
    "inc.": "incorporated",
    "file name": "filename",
    "file names": "filenames",
    "talent": "talon",
    "taryn": "terran",
    "pitch deque": "pitch deck",
    "ro": "row",
    "bites": "bytes",
    "lauder": "logger",
    "sub-": "sub",
    # "aunt": "ant",
    "a cell around her": "accelerometer",
    "a celeron matter": "accelerometer",
    "a celeron iter": "accelerometer",
    "a seller almond or": "accelerometer",
    "a celeron that are": "accelerometer",
    "a celeron matters": "accelerometers",
    "a seller matters": "accelerometers",
    "a solid ramen nurse": "accelerometers",
    "a celebration": "acceleration",
    "robot assist": "roboticist",
    "absalom": "epsilon",
    "fidgets": "phidgets",
    "yacht": "yaw",
    "ya": "yaw",
    "carl": "curl",
    "yamel": "yaml",
    "semicolon": ";",
    # "new-line": "\n",
    # "new-paragraph": "\n\n",
    "teak": "k",
    "virg": "v",
    "zug": "s",
    "pre-": "pre",
    "multi-": "multi",
    "in turn": "intern",
    "re- factor": "refactor",
    "re- factoring": "refactoring",
    "e-mail": "email",
    "fulsome": "folsom",
    "thumbs down": ":-1:",
    "thumbs-down": ":-1:",
    "thumbs up": ":+1:",
    "thumbs-up": ":+1:",
    "okay hand": ":ok_hand:",
    "thinking face": ":thinking_face:",
    "in-line": "in line",
    "jupiter": "jupyter",
    "pie": "py",
    ".pie": ".py",
    "dot pie": ".py",
    "dot by": ".py",
    "dot hi": ".py",
    ".hi": ".py",
    ". hi": ".py",
    ".by": ".py",
    "python three": "python3",
    "num py": "numpy",
    "K wargs": "kwargs",
    "dot shell": ".sh",
    "self-taught": "self.",
    "self-doubt": "self.",
    "pip installed": "pip install",
    "rapper": "wrapper",
    "stack trace": "stacktrace",
    "repose": "repos",
    "ellis": "elif",
    "tubal": "tuple",
    "deck": "deque",
    "log it's": "logits",
    "sell": "cell",
    "jeep you": "gpu",
    "endo": "end",
    "and oh": "end",
    "rappers": "wrappers",
    "poynter": "pointer",
    "numb": "num",
    "gnome": "num",
    "Phnom": "num",
    "don": "done",
    "jet": "git",
    "name space": "namespace",
    "name spaces": "namespaces",
    "g cloud": "gcloud",
    "voice code": "voicecode",
    "nirvana": "nervana",
    "terrace": "keras",
    "karis": "keras",
    "me on": "neon",
    "lennix": "linux",
    "cube nets": "kubernetes",
    "q burnett": "kubernetes",
    "cooper9": "kubernetes",
    "expand dimms": "expand dims",
    "dimms": "dims",
    "dems": "dims",
    "seek to seek": "Seq2Seq",
    "data set": "dataset",
    "data loader": "dataloader",
    "call back": "callback",
    "jim": "gym",
    "angie": "ng",
    "and g": "ng",
    "mg": "ng",
    "mp": "np",
    "and p": "np",
    "all the rhythms": "algorithms",
    "all rhythms": "algorithms",
    "waits": "weights",
    "wait": "weight",
    "dk": "decay",
    "epoque": "epoch",
    "epic": "epoch",
    "epoques": "epochs",
    "epics": "epochs",
    "1 hot": "onehot",
    "one hot": "onehot",
    "scaler": "scalar",
    "sql light": "sqlight",
    "post gress": "postgres",
    "sink": "sync",
    "and betting": "embedding",
    "I am betting": "embedding",
    "I'm betting": "embedding",
    "phil": "fill",
    "gam": "gan",
    "gann": "gan",
    "ncloud interactive": "ncloud interact",
    "adam": "atom",
    "pseudo-": "sudo",
    "pipe": "|",
    "apt get": "apt-get",
    "macron": "make run",
    "make show": "make shell",
    "standard out": "stdout",
    "standard in": "stdin",
    "standard error": "stderr",
    "les": "less",
    "doctor": "docker",
    "darker": "docker",
    "daughter": "docker",
    "docker file": "dockerfile",
    "communities": "kubernetes",
    "cube control": "kubectl",
    "shall": "shell",
    "w get": "wget",
    "backslash": "\\",
    "jet tub": "github",
    "git tub": "github",
    "jet hub": "github",
    "git hub": "github",
    "ron": "run",
    "thorpe": "\t",
    "tharp": "\t",
    "if not none": "if not None",
    "shayna": "shaina",
    "constance": "constants",
}

# Add vocabulary words (or phrases you want treated as words) here that aren't
# recognized by Talon and are written differently than they're pronounced.
mapping_vocabulary.update(dict(zip(simple_vocabulary, simple_vocabulary)))


mod = Module()


@mod.capture(rule="{user.vocabulary}")
def vocabulary(m) -> str:
    return m.vocabulary


@mod.capture(rule="(<user.vocabulary> | <word>)")
def word(m) -> str:
    try:
        return m.vocabulary
    except AttributeError:
        # TODO: if the word is both a regular word AND user.vocabulary, then in
        # principle it may parse as <word> instead; we ought to pass it through
        # mapping_vocabulary to be sure. But we should be doing that in
        # user.text, below, too.
        words = actions.dictate.replace_words(actions.dictate.parse_words(m.word))
        assert len(words) == 1
        return words[0]


punctuation = set(".,-!?;:")


@mod.capture(rule="(<user.vocabulary> | <phrase>)+")
def text(m) -> str:
    words = []
    for item in m:
        if isinstance(item, grammar.vm.Phrase):
            words.extend(
                actions.dictate.replace_words(actions.dictate.parse_words(item))
            )
        else:
            words.extend(item.split(" "))

    result = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation and words[i - 1][-1] not in ("/-("):
            result += " "
        result += word
    return result


@mod.capture(rule="([<user.text>])")
def optional_text(m) -> str:
    if hasattr(m, "text"):
        return m.text
    else:
        return ""


# TODO: should this be handled in a more generic way?
@mod.capture(rule="([<user.text>])")
def optional_snake_text(m) -> str:
    if hasattr(m, "text"):
        return "_".join(m.text.split(" "))
    else:
        return ""


mod.list("vocabulary", desc="user vocabulary")

ctx = Context()

# dictate.word_map is used by actions.dictate.replace_words to rewrite words
# Talon recognized. Entries in word_map don't change the priority with which
# Talon recognizes some words over others.
ctx.settings["dictate.word_map"] = word_map

# user.vocabulary is used to explicitly add words/phrases that Talon doesn't
# recognize. Words in user.vocabulary (or other lists and captures) are
# "command-like" and their recognition is prioritized over ordinary words.
ctx.lists["user.vocabulary"] = mapping_vocabulary
