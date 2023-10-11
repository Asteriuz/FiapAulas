import Image from "next/image";

export default function Camisa() {
  return <div className="flex flex-col gap-y-4">
    <h1 className="text-2xl">CAMISA</h1>
    <Image src="/produtos/camisa.jpg" width={300} height={300} alt="camisa" />
    </div>;
}