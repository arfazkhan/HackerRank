def designerPdfViewer(h, word):
    max_height = max(h[ord(char) - ord('a')] for char in word)
    area = max_height * len(word)
    return area
