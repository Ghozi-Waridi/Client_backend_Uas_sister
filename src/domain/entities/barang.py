from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Barang:
    id_barang: str
    nama_barang: str

    def validate(self) -> Optional[str]:
        if not self.id_barang or len(self.id_barang) > 50:
            return "ID Barang harus diisi dan maksimal 50 karakter"
        if not self.nama_barang or len(self.nama_barang) > 255:
            return "Nama Barang harus diisi dan maksimal 255 karakter"
        return None

    def to_dict(self) -> dict:
        return {"id_barang": self.id_barang, "nama_barang": self.nama_barang}

    @classmethod
    def from_dict(cls, data: dict) -> "Barang":
        return cls(
            id_barang=data.get("id_barang", ""), nama_barang=data.get("nama_barang", "")
        )
