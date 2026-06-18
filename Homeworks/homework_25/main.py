
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor



user_ids = [
 f"https://jsonplaceholder.typicode.com/posts?userId={ID}"
    for ID in range(1, 6)
]

def get_posts(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"User {id}: ჩამოტვირთვა ვერ მოხერხდა ({e}) - გამოტოვებულია")
        return []


def count_posts(all_posts):
    counts = {}
    for post in all_posts:
        counts[post["userId"]] = counts.get(post["userId"], 0) + 1
    return counts



def find_longest_post(all_posts):
    return max(all_posts, key=lambda x: len(x["body"]))



def average_title_length(all_posts):
    total = sum(len(post["title"]) for post in all_posts)
    return total / len(all_posts)




def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(get_posts, user_ids))
    filtered_results = [post for sublist in results for post in sublist]

    with ProcessPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(count_posts, filtered_results)
        f2 = executor.submit(find_longest_post, filtered_results)
        f3 = executor.submit(average_title_length, filtered_results)

    count_posts_result = f1.result()
    find_longest_post_result = f2.result()
    average_title_length_result = f3.result()


    print("==========================================")
    print("\t\t\tპოსტების ანალიზი")
    print("==========================================")
    print("მომხმარებელი""\t\t\t""პოსტების რაოდენობა")
    print("------------------------------------------")
    for user_id in sorted(count_posts_result.keys()):
        print(f"{"user " + str(user_id):<20}{count_posts_result[user_id]:>13}")

    print()
    print("ყველაზე გრძელი პოსტი: ")
    print(f"\tმომხმარებელი: User {find_longest_post_result["userId"]}")
    print(f"\tსათაური: {find_longest_post_result["title"]}")
    print(f"\tსიგრძე: {len(find_longest_post_result["body"])} სიმბოლო")

    print()

    print(f"სათაურების საშუალო სიგრძე: {average_title_length_result:.1f} სიმბოლო")
    print("==========================================")


if __name__ == "__main__":
    main()




















