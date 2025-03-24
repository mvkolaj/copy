import matplotlib.pyplot as plt
import torch

model = torch.load("genres.pth")
print(model['model']['lt.weight'])
for item in model:
    print(item)
coordinates = model["model"]["lt.weight"].numpy()

fig = plt.figure(figsize=(10, 10))

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axis('off')

for x in range(coordinates.shape[0]):
    plt.annotate(model["objects"][x], (coordinates[x,0], coordinates[x,1]),
                 bbox={"fc":"white", "alpha":0.9})

plt.savefig("genres.png")
