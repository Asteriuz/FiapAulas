import Link from "next/link";

export default function Navbar() {
  return (
    <ul className="mb-6 text-2xl">
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/produtos">Produtos</Link>
      </li>
    </ul>
  );
}
