#!/usr/bin/env python3
"""Module has a funtion that does element addition"""
def add_arrays(arr1, arr2):
    """Return element addition or none when lengths differ"""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
