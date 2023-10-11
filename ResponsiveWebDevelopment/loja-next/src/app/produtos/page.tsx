import Link from "next/link"

export default function Produtos() {
  return (
    <div>
      <ul className="text-lg">
        <li><Link href="/produtos/tenis">Tenis</Link></li>
        <li><Link href="/produtos/camisa">Camisa</Link></li>
        <li><Link href="/produtos/calca">Calça</Link></li>
        <li><Link href="/produtos/meia">Meia</Link></li>
      </ul>
    </div>
  );
}
