label_annotations:  str | None = None
label_images:       str | None = None
label_jpg:          str | None = None
label_jpeg:         str | None = None
label_xml:          str | None = None


def get_label_annotations() -> str:
    global label_annotations

    if label_annotations is None:
        set_label_annotations(
            'annotations'
        )

    return label_annotations

def set_label_annotations(
    value: str
) -> None:
    global label_annotations
    label_annotations = value


def get_label_images() -> str:
    global label_images

    if label_images is None:
        set_label_images(
            'images'
        )

    return label_images

def set_label_images(
    value: str
) -> None:
    global label_images
    label_images = value


def get_label_jpg() -> str:
    global label_jpg

    if label_jpg is None:
        set_label_jpg(
            'jpg'
        )

    return label_jpg

def set_label_jpg(
    value: str
) -> None:
    global label_jpg
    label_jpg = value


def get_label_jpeg() -> str:
    global label_jpeg

    if label_jpeg is None:
        set_label_jpeg(
            'jpeg'
        )

    return label_jpeg

def set_label_jpeg(
    value: str
) -> None:
    global label_jpeg
    label_jpeg = value


def get_label_xml() -> str:
    global label_xml

    if label_xml is None:
        set_label_xml(
            'xml'
        )

    return label_xml

def set_label_xml(
        value: str
) -> None:
    global label_xml
    label_xml = value
