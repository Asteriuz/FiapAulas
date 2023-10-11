import Image from "next/image";

export default function Calca() {
  return (
    <div className="flex flex-col gap-y-4">
      <h1 className="text-2xl">CALÇA</h1>
      <Image src="/produtos/calca.webp" width={300} height={300} alt="calca" />
    </div>
  );
}
