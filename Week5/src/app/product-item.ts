export interface ProductItem {
    id: number,
    productId: number | string,
    name: string,
    price: number,
    description: string,
    imageUrl: string | string[],
    rating: number,
    shareLink: string,
    likes: number
}