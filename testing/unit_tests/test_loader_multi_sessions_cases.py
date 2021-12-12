from testing.common_testing_util import path_data_multi_sessions_contrasts_tmp
from ivadomed.keywords import LoaderParamsKW, ContrastParamsKW


def case_data_multi_session_contrast():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [1, 2, 3, 4],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w", "FLAIR", "PD"]
        }
    }

    return loader_parameters, "df_ref.csv"


def case_data_multi_session_contrast_missing_session():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [1, 2, 3, 4],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w", "FLAIR", "PD"]
        }
    }

    return loader_parameters, "df_ref_missing_session.csv"


def case_data_multi_session_contrast_mismatching_target_suffix():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [1, 2, 3, 4],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2", "aa"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w", "FLAIR", "PD"]
        }
    }

    return loader_parameters, "df_ref_missing_session.csv"


def case_data_multi_session_contrast_missing_modality():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [1, 2, 3, 4],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w"]
        }
    }

    return loader_parameters, "df_ref_missing_modality.csv"


def case_data_target_specific_session_contrast():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [2, 3],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w", "FLAIR", "PD"]
        }
    }

    return loader_parameters, "df_ref_selective_session.csv"

def case_data_target_single_subject_with_session():
    loader_parameters = {
        LoaderParamsKW.MULTICHANNEL: "true",
        LoaderParamsKW.TARGET_SESSIONS: [5],
        LoaderParamsKW.TARGET_GROUND_TRUTH: "_lesion-manual-rater1",
        LoaderParamsKW.PATH_DATA: [path_data_multi_sessions_contrasts_tmp],
        LoaderParamsKW.TARGET_SUFFIX: ["_lesion-manual-rater1", "_lesion-manual-rater2"],
        LoaderParamsKW.EXTENSIONS: [".nii", ".nii.gz"],
        "roi_params": {"suffix": None, "slice_filter_roi": None},
        LoaderParamsKW.CONTRAST_PARAMS: {
            ContrastParamsKW.CONTRAST_LIST: ["T1w", "T2w", "FLAIR", "PD"]
        }
    }

    return loader_parameters, "df_ref_single_session.csv"

