import asyncio
import aiohttp
from urllib.parse import urlparse, urlunparse, urljoin
import os
from tqdm import tqdm

# Function to fetch the status code of a URL
async def fetch_status(session, url, progress_bar, results):
    try:
        async with session.get(url) as response:
            status = response.status
            if status != 500:
                results.append((url, status))
            progress_bar.update(1)  # Update progress bar after each request
            return url, status
    except Exception as e:
        progress_bar.update(1)  # Update progress bar even if failed
        return url, None

# Function to handle requests for a single base URL combined with multiple words as subdomains
async def fetch_all_statuses(base_url, words, result_folder):
    results = []
    parsed_base = urlparse(base_url)
    
    async with aiohttp.ClientSession() as session:
        # Initialize the progress bar with the total number of requests
        with tqdm(total=len(words), desc="Checking URLs", unit="url") as progress_bar:
            tasks = []
            for word in words:
                # Create a new domain with the word as a subdomain
                new_netloc = f"{word}.{parsed_base.netloc}"
                
                # Construct the new URL with the word as a subdomain
                new_url = urlunparse((
                    parsed_base.scheme,
                    new_netloc,
                    parsed_base.path,
                    parsed_base.params,
                    parsed_base.query,
                    parsed_base.fragment
                ))

                # Print the URL for debugging
                

                # Create a task for each URL request
                task = asyncio.create_task(fetch_status(session, new_url, progress_bar, results))
                tasks.append(task)

            # Wait for all tasks to complete and gather results
            await asyncio.gather(*tasks)

        # Create a valid filename from the base URL
        filename = parsed_base.netloc.replace('.', '_') + ".txt"

        # Full path for the result file
        result_file_path = os.path.join(result_folder, filename)

        # Save results to the specified file
        with open(result_file_path, 'w') as file:
            for url, status in results:
                file.write(f"URL: {url} | Status Code: {status}\n")

        # Print URLs with status codes other than 500
        if results:
            print("\nURLs with status codes other than 500 an 404:")
            for url, status in results:
                if status != 500 and status != 404:
                    print(f"URL: {url} | Status Code: {status}")

# Main function to run the asyncio event loop
def start_work_dns(base_url, word_file_path):
    # Open the file and read the words
    with open(word_file_path, "r") as my_file:
        # Reading the file line by line and stripping newline characters
        data_into_list = [line.strip() for line in my_file.readlines()]

    # Define the result folder (current directory in this case)
    result_folder = os.path.abspath(".")

    # Run the asyncio event loop
    asyncio.run(fetch_all_statuses(base_url, data_into_list, result_folder))
