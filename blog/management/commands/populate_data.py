from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):
        #deleting existing data
        Post.objects.all().delete()
        title =[
    "Understanding Machine Learning",
    "The Basics of Web Development",
    "Exploring Artificial Intelligence",
    "Getting Started with Python",
    "Introduction to Data Science",
    "Building a RESTful API",
    "Deep Learning Fundamentals",
    "Data Visualization Techniques",
    "Introduction to Blockchain",
    "The Future of Quantum Computing",
    "A Guide to Cloud Computing",
    "Essentials of Network Security",
    "Mastering JavaScript",
    "Guide to Digital Marketing",
    "Basics of Mobile App Development",
    "An Overview of IoT",
    "Natural Language Processing (NLP)",
    "Getting Started with React",
    "Developing with Node.js",
    "Exploring DevOps Practices",
]

        content=[
    "Machine learning is a branch of artificial intelligence focused on building systems that learn from data...",
    "Web development encompasses a range of skills and tools to build and maintain websites...",
    "Artificial intelligence is transforming industries with intelligent systems capable of learning...",
    "Python is a versatile programming language used in data science, web development, and more...",
    "Data science involves analyzing complex datasets to extract meaningful insights...",
    "RESTful APIs enable communication between clients and servers in web applications...",
    "Deep learning is a subset of machine learning that uses neural networks with multiple layers...",
    "Data visualization is essential for understanding data trends and patterns...",
    "Blockchain is a decentralized ledger technology offering transparency and security...",
    "Quantum computing leverages quantum mechanics to solve problems at unprecedented speeds...",
    "Cloud computing provides on-demand access to computing resources over the internet...",
    "Network security protects information and systems from cyber threats...",
    "JavaScript is a powerful language for adding interactivity to websites...",
    "Digital marketing uses online channels to reach and engage customers...",
    "Mobile app development requires a mix of design and programming skills...",
    "The Internet of Things (IoT) connects everyday devices to the internet...",
    "NLP enables computers to understand and generate human language...",
    "React is a popular JavaScript library for building user interfaces...",
    "Node.js allows for server-side programming using JavaScript...",
    "DevOps integrates software development and IT operations for faster deployment...",
   
]

        img_url =[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
]
        #I am generating category in random by importing random module
        categories = Category.objects.all()
        for title, content, img_url in zip(title, content, img_url):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)
        
        self.stdout.write(self.style.SUCCESS("completed inserting data."))
