def threshold_image(image, threshold):
    data = image.get_data()
    idx_on = data[:,:,:] >= threshold
    idx_off = data[:,:,:] < threshold
    data[idx_on] = 1
    data[idx_off] = 0
