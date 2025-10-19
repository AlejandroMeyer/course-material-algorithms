import pytest
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions' / 'data_structures'))

from doubly_linked_list import DoublyLinkedList

@pytest.fixture
def song_list():
    dll = DoublyLinkedList()
    dll.append(("Song 1", "Artist A"))
    dll.append(("Song 2", "Artist B"))
    dll.append(("Song 3", "Artist C"))
    return dll

def test_append_song(song_list):
    assert song_list.to_list_forward() == [
        ("Song 1", "Artist A"),
        ("Song 2", "Artist B"),
        ("Song 3", "Artist C")
    ]
    assert song_list.to_list_backward() == [
        ("Song 3", "Artist C"),
        ("Song 2", "Artist B"),
        ("Song 1", "Artist A")
    ]

def test_play_next(song_list):
    assert song_list.current_data() == ("Song 1", "Artist A")
    assert song_list.play_next() == ("Song 2", "Artist B")
    assert song_list.play_next() == ("Song 3", "Artist C")
    assert song_list.play_next() is None  # No next song

def test_play_previous(song_list):
    song_list.play_next()  # Move to "Song 2"
    song_list.play_next()  # Move to "Song 3"
    assert song_list.play_previous() == ("Song 2", "Artist B")
    assert song_list.play_previous() == ("Song 1", "Artist A")
    assert song_list.play_previous() is None  # No previous song