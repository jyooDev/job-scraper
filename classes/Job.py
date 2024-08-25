from dataclasses import dataclass

@dataclass
class Job:
    title: str 
    company: str 
    region: str = "N/A"
    link: str = "N/A"

