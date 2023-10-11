import Image from "next/image";

export default function Meia() {
  return (
    <div className="flex flex-col gap-y-4">
      <h1 className="text-2xl">MEIA</h1>
      <Image src="/produtos/meia.webp" width={300} height={300} alt="meia" />
    </div>
  );
}
