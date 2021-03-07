
def build_annotation_mapping(df):
    """
    For a given source, select gold standard match mapping
    from the overall annotations file.
    :param df: DataFrame with annotations
    :return: dictionary with gold standard mapping
    """

    gold_standard_mapping = dict()
    hp_ids = df["ID"].values.tolist()

    source_ids = df["ID2"].values.tolist()
    # if pandas read ID as an float, then convert to int
    # and then string since matches data is loaded like that
    source_ids = [str(int(x)) if type(x) == float else str(x)
                  for x in source_ids]
    source_match_values = df["match"].values.tolist()

    for i, hp_id in enumerate(hp_ids):
        gold_standard_mapping[(hp_id, source_ids[i])] = source_match_values[i]
    return gold_standard_mapping


def evaluate_matches(predictions, gold_standard_dict):
    """
    Given predictions set and the gold standard, evaluate Precision, Recall and F1-Score.
    """
    # annotated as "Yes" and algorithm outputs "Match"
    num_true_positives = 0
    # annotated as "No" but algorithm outputs "Match"
    num_false_positives = 0
    # annotated as "Yes" and algorithm outputs "No Match"
    num_false_negatives = 0
    # annotated as "No" and algorithm outputs "No Match"
    num_true_negatives = 0

    for match_pair in predictions:
        if gold_standard_dict.get(match_pair, None) == 1:
            num_true_positives += 1

        elif gold_standard_dict.get(match_pair, None) == 0:
            num_false_positives += 1

    not_found_matches = set(gold_standard_dict).difference(
        set(predictions))

    for id_pair in not_found_matches:

        if gold_standard_dict.get(id_pair, None) == 1:
            num_false_negatives += 1

        elif gold_standard_dict.get(id_pair, None) == 0:
            num_true_negatives += 1

    if num_true_positives + num_false_positives:
        precision_ = num_true_positives / (
            num_true_positives + num_false_positives)
    else:
        precision_ = 0.0

    if num_true_positives + num_false_negatives:
        recall_ = num_true_positives / (
            num_true_positives + num_false_negatives)
    else:
        recall_ = 0.0

    if precision_+recall_ >0.0:
        f1_score = "{0:.2f}".format(
            round(2 * ((precision_ * recall_) / (precision_ + recall_)),
                  4) * 100)
    else:
        f1_score = 0.0

    return recall_, precision_, f1_score