import Image from "next/image";

export default function Tenis() {
  return (
    <div className="flex flex-col gap-y-4">
      <h1 className="text-2xl">TENIS</h1>
      <Image src="/produtos/tenis.webp" width={300} height={300} alt="tenis" />
    </div>
  );
}
