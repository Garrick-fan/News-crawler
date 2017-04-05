class Paragraph(object):
  def __init__(self, enParagraph, chParagraph):
    self.EnParagraph = enParagraph
    self.ChParagraph = chParagraph

  def __str__(self):  
      content  = "EN:" + self.EnParagraph + "\n"
      content += "CH:" + self.ChParagraph + "\n"
      return content

