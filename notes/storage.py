from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from itertools import count


@dataclass
class Note:
    id: int
    text: str
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(timespec="seconds")
    )

    def to_dict(self):
        return asdict(self)


class NoteStorage:
    """Простое хранилище заметок в памяти."""

    def __init__(self):
        self._notes: dict[int, Note] = {}
        self._ids = count(1)

    def list(self):
        return sorted(self._notes.values(), key=lambda n: n.id, reverse=True)

    def get(self, note_id):
        return self._notes.get(note_id)

    def add(self, text):
        note = Note(id=next(self._ids), text=text)
        self._notes[note.id] = note
        return note

    def delete(self, note_id):
        return self._notes.pop(note_id, None) is not None
