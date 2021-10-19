import tika

tika.initVM()

from tika import parser


def convert(path):
    with open(path + ".txt", "wb") as output:
        output.write(parser.from_file(path)['content'].encode("UTF-8"))


convert('training_data_pdfs/Top 10 Paris.pdf')
convert('training_data_pdfs/Lessons from Madame Chic.pdf')
convert('training_data_pdfs/Basics Fashion Design.pdf')
convert('training_data_pdfs/Marie Antoinette.pdf')
convert('training_data_pdfs/The Luxury Strategy.pdf')
convert('training_data_pdfs/Creative Fashion Drawing.pdf')
