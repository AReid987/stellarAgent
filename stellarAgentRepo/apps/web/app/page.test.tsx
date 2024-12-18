import { render, screen } from "@testing-library/react";
import Page from "./page";

describe("Page", () => {
  it("renders a list", () => {
    render(<Page />);
    const list = screen.getByRole("list");
    expect(list).toBeInTheDocument();
  });
});
