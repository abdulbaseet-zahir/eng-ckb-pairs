import os
import logging
import pandas as pd

# Configure the logging level and format
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


ckb_eng_links_url = (
    "https://downloads.tatoeba.org/exports/per_language/ckb/ckb-eng_links.tsv.bz2"
)

ckb_sentences_detailed_url = "https://downloads.tatoeba.org/exports/per_language/ckb/ckb_sentences_detailed.tsv.bz2"

eng_sentences_detailed_url = "https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences_detailed.tsv.bz2 "


class Tatoeba:
    def __init__(
        self,
    ):
        pass

    def bz2url_to_df(self, url: str):
        logging.info(f"Downloading {url}...")
        return pd.read_csv(url, sep="\t", header=None, compression="bz2")

    def download_eng_ckb_data_from_tatoeba(
        self,
        ckb_eng_links_url: str = ckb_eng_links_url,
        ckb_sentences_detailed_url: str = ckb_sentences_detailed_url,
        eng_sentences_detailed_url: str = eng_sentences_detailed_url,
    ):
        ckb_eng_links = self.bz2url_to_df(ckb_eng_links_url)
        ckb_sentences_detailed = self.bz2url_to_df(ckb_sentences_detailed_url)
        eng_sentences_detailed = self.bz2url_to_df(eng_sentences_detailed_url)

        logging.info("Downloading complete!")

        ckb_eng_links.columns = ["ckb_id", "eng_id"]
        ckb_sentences_detailed.columns = [
            "ckb_id",
            "language",
            "ckb_sentence",
            "ckb_username",
            "created_date",
            "updated_date",
        ]
        eng_sentences_detailed.columns = [
            "eng_id",
            "language",
            "eng_sentence",
            "eng_username",
            "created_date",
            "updated_date",
        ]
        data = pd.merge(
            pd.merge(ckb_eng_links, ckb_sentences_detailed, on="ckb_id"),
            eng_sentences_detailed,
            on="eng_id",
        )[
            [
                "eng_id",
                "ckb_id",
                "eng_sentence",
                "ckb_sentence",
                "eng_username",
                "ckb_username",
            ]
        ]

        data.to_csv(
            os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t", index=False
        )

    def get_data(
        self,
        data_path: str = "data",
        source="eng_ckb_tatoeba",
    ):
        self.data_path = data_path
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        if source == "eng_ckb_tatoeba":
            try:
                return pd.read_csv(
                    os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t"
                )
            except:
                self.download_eng_ckb_data_from_tatoeba()
                return pd.read_csv(
                    os.path.join(self.data_path, "eng_ckb_tatoeba.tsv"), sep="\t"
                )
        else:
            raise ValueError(
                f"Invalid source. Please choose from {self.get_data_sources()}"
            )

    def get_data_sources(self):
        return ["eng_ckb_tatoeba"]
