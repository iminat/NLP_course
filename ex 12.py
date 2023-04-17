import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
text = "Endangered species are a major concern for governments, scientists, academics, and conservation groups all around the world. Many countries have laws that provide special protection to endangered species or their habitats. These laws may forbid hunting, restrict land development, or create nature preserves to safeguard the survival of endangered species. Despite the efforts of conservationists, only a few of the many endangered species actually make it to the lists and obtain legal protection. Many more species become extinct, or potentially will become extinct, without gaining public notice. The ICUN (the World Conservation Union) is the organization that governments, scientists, academics, and conservation groups rely on for the designation of a species as endangered. The ICUN sets the criteria for classifying a species as critically endangered or endangered. According to the ICUN, a species is critically endangered when it meets any of the following criteria: its population has been reduced by 90 percent in the last ten years; its population has been reduced over 80 percent in the last ten years, where the cause of reduction has not been stopped or is determined to be irreversible; its population is expected to be reduced by 80 percent in the next ten years or three generations, whichever is longer, up to a maximum of 100 years; or its population size is estimated to be 250 mature species or less. The ICUN states that a species is considered endangered when the species meets any of the following criteria: its population has been reduced by 70 percent in the last ten years; its population has been reduced over 50 percent in the last ten years, where the cause of reduction has not been stopped or is determined to be irreversible; its population is suspected to be reduced by 50 percent in the next ten years or three generations, whichever is longer, up to a maximum of 100 years; or the species is known to exist in five or fewer geographic locations. Some of the more well-known endangered species include the giant panda, some whales and dolphins, rhinoceroses, elephants, marine turtles, and the great apes. However, there are many more endangered species that are less well-known to the general public but play a crucial role in maintaining the balance and integrity of ecosystems. The laws protecting endangered species are not without controversy. There are debates around the criteria for placing a species on the endangered species list, and the criteria for removing a species from the list once its population has recovered. There are also debates around whether restrictions on land development constitute a taking of land by the government, and whether private landowners should be compensated for the loss of use of their land. Obtaining reasonable exceptions to protection laws is another area of controversy. Conservation policies sometimes call for the reintroduction of an endangered species to an ecosystem, such as the repopulation of Yellowstone Park with gray wolves brought from Canada in 1995. However, such reintroductions are an art science, rather than an exact science, as there are too many variables to be sure what will happen. There are examples throughout history of good intentions having undesirable consequences, such as efforts to manage the Everglades leading to catastrophic exaggerations of the flood-and-drought cycle, or the elimination of DDT exacerbating the problem of malaria in Africa. As a result, humans need to have the humility to recognize the uncertainty involved in conservation policy that involves changing nature or working with a complex ecosystem. Being listed as an endangered species can sometimes have unintended consequences. It could make a species more desirable for collectors and poachers. However, this is usually considered a spurious argument by those who favor loose protection laws."

tokens = word_tokenize(text)
print(tokens[:20])

pos_tags = nltk.pos_tag(tokens)
print(pos_tags[:20])

stop_words = set(stopwords.words('english'))
filtered_tokens = []
for token in tokens:
    if token.lower() not in stop_words:
        filtered_tokens.append(token)
print(filtered_tokens[:20])

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed_tokens = []
for token in filtered_tokens:
    stemmed_token = stemmer.stem(token)
    stemmed_tokens.append(stemmed_token)
print(stemmed_tokens[:20])


