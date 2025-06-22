import requests

BASE_URL = "https://api.petfinder.com/v2"

# Retrieve a list of all animal types available on Petfinder.
def test_get_animal_types(headers):
    response = requests.get(f"{BASE_URL}/types", headers=headers)
    #print("\nAnimal Types Response JSON:", response.json())
    
    assert response.status_code == 200

    animal_types = [animal["name"] for animal in response.json()["types"]]
    print("Extracted Animal Types:", animal_types)
    
    # Verify that "Dog" is one of the animal types returned.  
    assert "Dog" in animal_types


def test_get_dog_breeds(headers):
    # Retrieve a list of all dog breeds available on Petfinder.
    response = requests.get(f"{BASE_URL}/types/dog/breeds", headers=headers)
    #print("\nDog Breeds Response JSON:", response.json())

    assert response.status_code == 200

    breed_names = [breed["name"] for breed in response.json()["breeds"]]
    print("Extracted Dog Breeds:", breed_names)
    
    assert "Golden Retriever" in breed_names


# Perform a search for dogs of the "Golden Retriever" breed and verify that at least one result is returned.  
def test_search_golden_retriever(headers):
    params = {
        "type": "dog",
        "breed": "Golden Retriever"
    }
    response = requests.get(f"{BASE_URL}/animals", headers=headers, params=params)
    #print("\nGolden Retriever Search Response JSON:", response.json())

    assert response.status_code == 200

    animals = response.json().get("animals", [])
    print(f"Number of Golden Retrievers Found: {len(animals)}")
    if animals:
        print("First Result Preview:", animals[0])

    assert len(animals) > 0
