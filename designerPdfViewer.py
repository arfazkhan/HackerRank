#ProblemStatement:
#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

def designerPdfViewer(h, word):
    max_height = max(h[ord(char) - ord('a')] for char in word)
    area = max_height * len(word)
    return area

#Logic:
#First, I find the maximum height of the letters in the word from the given heights list. Then, I multiply this maximum height by the length of the word to get the total area. It's like finding the highlighted space in the PDF viewer, where the height is determined by the tallest letter and the width is the length of the word.
