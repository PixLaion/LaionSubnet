from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

prompts = [
    'Create an image of a cozy autumn picnic spread on a rustic wooden table, featuring a steaming mug of apple cider, a slice of pumpkin pie with a dollop of whipped cream, a plaid blanket, colorful fall leaves scattered around, and a basket of freshly picked apples.',
    'Create an image of a bustling city street at night, with neon signs illuminating the sidewalk and people huddled in warm coats.',
    'Create an image of a serene beach at sunset, with the waves gently lapping at the shore and a lighthouse in the distance.',
    'Create an image of a dense forest with sunlight filtering through the leaves, creating a mosaic of light and shadow on the forest floor.',
    'Create an image of a snowy mountain peak against a clear blue sky, with a lone climber making their way to the summit.',
    'Create an image of a tranquil lake reflecting the surrounding mountains and the sky at dawn.',
    'Create an image of a bustling marketplace in a historic city, with vendors selling colorful spices, textiles, and pottery.',
    'Create an image of a modern city skyline at dusk, with skyscrapers lit up against the twilight sky.',
    'Create an image of a quiet country road winding through fields of blooming sunflowers.',
    'Create an image of a tropical beach with palm trees swaying in the breeze and a hammock strung between two trees.',
    'Create an image of a cozy cabin in the woods, with smoke curling up from the chimney and a light snowfall outside.',
    'Create an image of a vibrant coral reef teeming with colorful fish and other marine life.',
    'Create an image of a hot air balloon floating over a patchwork of farmland and small towns.',
    'Create an image of a tranquil Japanese garden with a koi pond, a stone lantern, and cherry blossom trees in full bloom.',
    'Create an image of a bustling coffee shop on a rainy day, with people reading, chatting, and sipping their drinks.',
    'Create an image of a starry night sky over a desert landscape, with a campfire flickering in the foreground.',
    'Create an image of a charming European village with cobblestone streets, flower-filled window boxes, and a central square with a fountain.',
    'Create an image of a safari scene with elephants, zebras, and giraffes grazing on the African savannah.',
    'Create an image of a peaceful yoga studio with natural light, hardwood floors, and people in various yoga poses.',
    'Create an image of a lively music festival with a crowd of people dancing and a band playing on stage.',
    'Create an image of a serene tea plantation with rows of tea bushes and workers picking leaves.',
    'Create an image of a bustling train station with people rushing to catch their trains and a large clock on the wall.',
    'Create an image of a cozy library with tall bookshelves, comfortable armchairs, and people engrossed in their books.',
    'Create an image of a vibrant street art mural on a brick wall in an urban setting.',
    'Create an image of a tranquil zen garden with raked sand, rocks, and a small wooden bridge.',
    'Create an image of a lively carnival with a ferris wheel, cotton candy stands, and children playing games.',
    'Create an image of a peaceful Buddhist temple in the mountains, with monks in saffron robes and prayer flags fluttering in the wind.',
    'Create an image of a bustling sushi bar in Tokyo, with chefs preparing sushi and customers seated around the counter.',
    'Create an image of a romantic Parisian street with a sidewalk cafe, a flower shop, and the Eiffel Tower in the distance.',
    'Create an image of a tranquil lavender field in Provence, with rows of purple flowers and a farmhouse in the distance.',
    'Create an image of a lively jazz club with a saxophonist playing on stage and people dancing.',
    'Create an image of a peaceful morning in a yoga retreat, with people meditating in a lush garden.',
    "Create an image of a bustling farmer's market with stalls selling fresh fruits, vegetables, and homemade goods.",
    'Create an image of a tranquil canoe trip on a calm lake, with a forest of autumn colors on the shore.',
    'Create an image of a lively tapas bar in Spain, with people sharing small plates of food and glasses of wine.',
    'Create an image of a peaceful morning in a mountain cabin, with a cup of coffee on the porch overlooking the forest.',
    'Create an image of a bustling bakery with fresh bread and pastries on display and a baker kneading dough.',
    'Create an image of a tranquil koi pond in a Japanese garden, with a red bridge and cherry blossom trees.',
    'Create an image of a lively beach party with people playing volleyball, surfing, and enjoying the sun.',
    'Create an image of a peaceful olive grove in Tuscany, with rows of olive trees and a rustic farmhouse.',
    'Create an image of a bustling dim sum restaurant in Hong Kong, with servers pushing carts of steaming dumplings.'
]

# Convert the prompts to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(prompts)

# Cluster the prompts using KMeans
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# Create a list of lists to store the prompts in their respective clusters
clustered_prompts = [[] for _ in range(5)]

# Assign each prompt to a cluster
for i, label in enumerate(kmeans.labels_):
    clustered_prompts[label].append(prompts[i])

for i, cluster in enumerate(clustered_prompts):
    print(f'Cluster {i + 1}:{len(cluster)}:')
    for prompt in cluster:
        print(prompt)
    print()



