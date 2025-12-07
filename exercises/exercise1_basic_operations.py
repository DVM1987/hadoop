#!/usr/bin/env python3
"""
Exercise 1: Basic HDFS Operations
Level: Beginner

Learning Objectives:
- Connect to HDFS using Python
- Create directories in HDFS
- Upload and download files
- List directory contents
- Get file information

Tasks:
1. Connect to the HDFS cluster
2. Create a directory structure /exercises/exercise1/
3. Upload the sample_employees.csv file to HDFS
4. List the contents of your directory
5. Download the file back to a different location
6. Display file information (size, replication factor, etc.)
"""

from hdfs import InsecureClient
import os

def exercise1():
    """Complete the basic HDFS operations"""
    
    # TODO: Task 1 - Connect to HDFS
    # Initialize HDFileSystem with namenode host and port
    # hdfs = None  # Replace with your connection
    try:
        hdfs = InsecureClient('http://namenode:9870')
        print("Connected to HDFS")
    except Exception as e:
        print(f"Error connecting to HDFS: {e}")
        raise e

    # TODO: Task 2 - Create directory structure
    # Create /exercises/exercise1/ directory
    # using try except to handle the error
    try:
        hdfs.makedirs('/exercises/exercise1/')
        print("Directory created: /exercises/exercise1/")
    except Exception as e:
        print(f"Error creating directory: {e}")
        raise e

    
    # TODO: Task 3 - Upload file
    # Upload /data/sample_employees.csv to /exercises/exercise1/employees.csv
    try:
        hdfs.upload('/exercises/exercise1/employees.csv', '/data/sample_employees.csv')
        print("File uploaded: /data/sample_employees.csv to /exercises/exercise1/employees.csv")
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise e
    
    # TODO: Task 4 - List directory contents
    # List and print the contents of /exercises/exercise1/
    try:
     
        contents = hdfs.list('/exercises/exercise1/', status=True)
        print("Directory contents:")
        for item in contents:
            print(f"  {item[0]} - Size: {item[1]['length']} bytes")
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        raise e
    
    # TODO: Task 5 - Download file
    # Download the file to local filesystem
    try:
        hdfs.download('/exercises/exercise1/employees.csv', '/tmp/downloaded_employees.csv')
        print("File downloaded: /exercises/exercise1/employees.csv to /tmp/downloaded_employees.csv")
    except Exception as e:
        print(f"Error downloading file: {e}")
        raise e
    # TODO: Task 6 - Display file information
    # Get and print file information for the uploaded file
    try:
        info = hdfs.status('/exercises/exercise1/employees.csv')
        print("File information:")
        print(f"  Name: /exercises/exercise1/employees.csv")
        print(f"  Size: {info['length']} bytes")
        print(f"  Replication: {info['replication']}")
        print(f"  Block size: {info['blockSize']} bytes")
    except Exception as e:
        print(f"Error getting file information: {e}")
        raise e
    print("Exercise 1 completed!")

if __name__ == "__main__":
    exercise1()

# Expected Output:
"""
Directory created: /exercises/exercise1/
File uploaded successfully
Directory contents:
  /exercises/exercise1/employees.csv - Size: XXX bytes
File downloaded successfully
File Info:
  Name: /exercises/exercise1/employees.csv
  Size: XXX bytes
  Replication: 2
  Block size: XXXXXXX bytes
Exercise 1 completed!
"""

# Hints:
"""
1. Use InsecureClient('http://namenode:9870') to connect
2. Use hdfs.makedirs(path) to create directories
3. Use hdfs.upload(hdfs_path, local_path) for uploads
4. Use hdfs.list(path, status=True) to list contents
5. Use hdfs.download(hdfs_path, local_path) for downloads
6. Use hdfs.status(path) to get file information
"""
