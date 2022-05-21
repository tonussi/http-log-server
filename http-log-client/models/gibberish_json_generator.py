from gibberish import Gibberish

class GibberishHttpJson():
    def __init__(self, key_range=100000, as_json=False, **kwargs) -> None:
        self.gib = Gibberish()
        self.extra_configuration = kwargs
        self.json_data = self._generate_json(key_range)
        self.as_json = as_json

    def perform(self):
        if self.as_json: return self.json_data

        return self._json_content_stringfy()

    # private

    def _json_content_stringfy(self):
        return str(self.json_data).replace('"', '\"').replace("'", '\"')

    def _build_batch_with_gibberish(self, key_range):
        batch = []

        for _ in range(key_range):
            batch.append(
                {
                    "operation": "INSERT",
                    "name": self.gib.generate_word(start_vowel=True),
                    "city": self.gib.generate_word(start_vowel=True)
                }
            )

        return batch

    def _generate_json(self, key_range=100000):
        return { **self.extra_configuration, "batch": self._build_batch_with_gibberish(key_range)}
