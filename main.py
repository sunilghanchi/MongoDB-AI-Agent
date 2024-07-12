import streamlit as st
from pymongo import MongoClient
import urllib,io,json
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm=ChatGroq(model="llama3-8b-8192",temperature=0.0,api_key="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")
#mongo client
username="sunilghanchi24"
pwd="G3urZVqz929lSkPW"
client=MongoClient("mongodb+srv://"+urllib.parse.quote(username)+":"+urllib.parse.quote(pwd)+"@first-cluster.te5qmyv.mongodb.net/?retryWrites=true&w=majority&appName=first-cluster")

db=client["sample_airbnb"]
collection=db["listingsAndReviews"]

st.title("Talk to MongoDB")
st.write("Ask Anything and Get Answer")
input=st.text_area("enter your question here")

with io.open("sample.txt","r",encoding="utf-8")as f1:
    sample=f1.read()
    f1.close()

prompt="""
        you are a very intelligent AI assitasnt who is expert in identifying relevant questions fro user
        from user and converting into nosql mongodb agggregation pipeline query.
        Note: You have to just return the query as to use in agggregation pipeline nothing else. Don't return any other thing
        Please use the below schema to write the mongodb queries , dont use any other queries.
       schema:
       the mentioned mogbodb collection talks about listing for an accommodation on Airbnb. The schema for this document represents the structure of the data, describing various properties related to the listing, host, reviews, location, and additional features. 
       your job is to get python code for the user question
       Please only provide the only query, don't provide any other text than query.
       Here’s a breakdown of its schema with descriptions for each field:

1. **_id**: Unique identifier for the listing.
2. **listing_url**: URL to the listing on Airbnb.
3. **name**: Name of the listing.
4. **summary**: A brief summary of the listing.
5. **space**: Description of the space provided.
6. **description**: Full description of the listing.
7. **neighborhood_overview**: Overview of the neighborhood.
8. **notes**: Additional notes provided by the host.
9. **transit**: Information about local transit options.
10. **access**: Information about what parts of the property guests can access.
11. **interaction**: Description of how the host will interact with the guests.
12. **house_rules**: House rules that guests must follow.
13. **property_type**: Type of property (e.g., House, Apartment).
14. **room_type**: Type of room (e.g., Entire home/apt, Private room).
15. **bed_type**: Type of bed provided.
16. **minimum_nights**: Minimum number of nights required for booking.
17. **maximum_nights**: Maximum number of nights allowed for booking.
18. **cancellation_policy**: Cancellation policy for the listing.
19. **last_scraped**: Date when the data was last scraped.
20. **calendar_last_scraped**: Date when the calendar was last scraped.
21. **first_review**: Date of the first review.
22. **last_review**: Date of the last review.
23. **accommodates**: Number of guests the listing accommodates.
24. **bedrooms**: Number of bedrooms.
25. **beds**: Number of beds.
26. **number_of_reviews**: Total number of reviews.
27. **bathrooms**: Number of bathrooms.
28. **amenities**: List of amenities provided.
29. **price**: Nightly price for the listing.
30. **security_deposit**: Amount of the security deposit.
31. **cleaning_fee**: Cleaning fee charged.
32. **extra_people**: Fee for extra guests.
33. **guests_included**: Number of guests included in the booking price.
34. **images**: Object containing URLs for various images of the listing.
35. **host**: Object containing information about the host.
36. **address**: Object containing detailed address of the listing.
37. **availability**: Object detailing availability for different time spans (30, 60, 90, and 365 days).
38. **review_scores**: Object containing different review scores (overall, accuracy, cleanliness, checkin, communication, location, value).
39. **reviews**: Array of review objects, each containing details about individual reviews.

##Embedded Objects

**Host Details:**
   - **host_id**: Unique identifier for the host.
   - **host_url**: URL to the host’s profile.
   - **host_name**: Name of the host.
   - **host_since**: Date when the host joined Airbnb.
   - **host_location**: Location of the host.
   - **host_about**: Information about the host.
   - **host_response_time**: Average response time of the host.
   - **host_response_rate**: Host's response rate.
   - **host_acceptance_rate**: Rate at which the host accepts reservations.
   - **host_is_superhost**: Whether the host is a superhost.
   - **host_thumbnail_url**: URL to the host's thumbnail image.
   - **host_picture_url**: URL to the host's picture.
   - **host_neighbourhood**: Neighbourhood of the host.
   - **host_listings_count**: Number of listings the host has.
   - **host_total_listings_count**: Total number of listings including joint listings.
   - **host_verifications**: List of verifications the host has completed.
   - **host_has_profile_pic**: Whether the host has a profile picture.
   - **host_identity_verified**: Whether the host's identity has been verified.

**Address Details:**
   - **street**: Street address of the listing.
   - **suburb**: Suburb in which the listing is located.
   - **government_area**: Government area the listing belongs to.
   - **market**: Market area for the listing.
   - **country**: Country where the listing is located.
   - **country_code**: Country code for the listing.
   - **location**: Object containing geographical coordinates (longitude, latitude).

**Location Object:**
   - **type**: Type of location data (Point).
   - **coordinates**: Array of coordinate values (longitude, latitude).
   - **is_location_exact**: Whether the location is exact.

**Images Object:**
   - **thumbnail_url**: URL of the thumbnail image.
   - **medium

_url**: URL of the medium-sized image.
   - **picture_url**: URL of the picture.
   - **xl_picture_url**: URL of the extra-large picture.

##Arrays

**Amenities**:
   - List of amenities available at the listing (e.g., Wifi, Kitchen, etc.).

**Reviews**:
   - **_id**: Unique identifier for the review.
   - **date**: Date of the review.
   - **listing_id**: ID of the listing reviewed.
   - **reviewer_id**: ID of the reviewer.
   - **reviewer_name**: Name of the reviewer.
   - **comments**: Text of the comment left by the reviewer.

This schema provides a comprehensive view of the data structure for an Airbnb listing in MongoDB, 
including nested and embedded data structures that add depth and detail to the document.
use the below sample_examples to generate your queries perfectly
sample_example:

Below are several sample user questions related to the MongoDB document provided, 
and the corresponding MongoDB aggregation pipeline queries that can be used to fetch the desired data.
Use them wisely.

sample_question: {sample}
As an expert you must use them whenever required.
Note: You have to just return the query nothing else. Don't return any additional text with the query.Please follow this strictly
input:{question}
output:
"""
query_with_prompt=PromptTemplate(
    template=prompt,
    input_variables=["question","sample"]
)

final_prompt=PromptTemplate(
    template="""
    You have the MongoDB question and the Query output below, you have to convert the query output into natural language as user asked the question:
    Only write the answer after formatting it but nothing other thing is require than answer.
    Question : {question},
    Query Output: {results}
    Final Output:
    """,
    input_variables=["question","results"]
)

llmchain=LLMChain(llm=llm,prompt=query_with_prompt,verbose=True)

if input is not None:
    button=st.button("Submit")
    if button:
        response=llmchain.invoke({
            "question":input,
            "sample":sample
        })
        print(response)

        query=json.loads(response["text"])
        print(query)
        results=collection.aggregate(query)
        for result in results:
            final_result=LLMChain(llm=llm,prompt=final_prompt)
            if results is not None:
                final_response=final_result.invoke({
                    "question":input,
                    "results":result
                })
                final = final_response["text"]
                st.write(final)


