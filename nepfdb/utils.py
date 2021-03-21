from PIL import Image, ExifTags


def checkNumberAndAlpha(value):
    """Check if string contains at least one number
    and an alphabet"""
    is_alpha = False
    is_num = False

    for i in str(value):
        if i.isalpha():
            is_alpha = True

        if i.isdigit():
            is_num = True

    return is_alpha and is_num


def checkAlphaAndSpace(value):
    value = str(value).strip()
    return all(x.isalpha() or x.isspace() for x in value)


def image_crop(obj):
    """ Crop image of the object.

        Must: Have get_image() function inside class which returns photo_attribute.path

        Param: object, object where one of attribute must have image field

        Return: None
     """
    img = Image.open(obj.get_image())
    width, height = img.size  # Get dimensions

    ''' When a picture is taller than it is wide, it means the camera was rotated. Some cameras can detect this and write that info
        in the picture's EXIF metadata. Some viewers take note of this metadata and display the image appropriately. 
        To check the orientation and rotate if needed
        https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
    '''
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(img._getexif().items())

        if exif[orientation] == 3:
            img = img.rotate(180)
        elif exif[orientation] == 6:
            img = img.rotate(270)
        elif exif[orientation] == 8:
            img = img.rotate(90)
    except:
        pass

    if width > 250 and height > 250:
        # keep ratio but shrink down
        img.thumbnail((width, height))

    # check which one is smaller
    if height < width:
        # make square by cutting off equal amounts left and right
        left = (width - height) / 2
        right = (width + height) / 2
        top = 0
        bottom = height
        img = img.crop((left, top, right, bottom))

    elif width < height:
        # make square by cutting off bottom
        left = 0
        right = width
        top = (height - width)/2
        bottom = (height + width)/2
        img = img.crop((left, top, right, bottom))

    if width > 250 and height > 250:
        img.thumbnail((250, 250))

    return img.save(obj.get_image())
