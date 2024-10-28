import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

describe("Frontend Layout Tests", () => {
  test("Header layout and components", () => {
    render(<App />);
    const header = screen.getByRole("banner");
    expect(header).toHaveStyle("display: flex");

    const logo = screen.getByAltText("Logo");
    expect(logo).toBeInTheDocument();

    const deliveryInfo = screen.getByText(/delivery information/i);
    expect(deliveryInfo).toBeInTheDocument();

    const searchBar = screen.getByRole("searchbox");
    expect(searchBar).toBeInTheDocument();

    const languageSelection = screen.getByText(/language/i);
    const accountDetails = screen.getByText(/account/i);
    const orders = screen.getByText(/orders/i);
    const cart = screen.getByRole("button", { name: /cart/i });
    expect(languageSelection).toBeInTheDocument();
    expect(accountDetails).toBeInTheDocument();
    expect(orders).toBeInTheDocument();
    expect(cart).toBeInTheDocument();
  });

  test("Navigation bar layout", () => {
    const navBar = screen.getByRole("navigation");
    expect(navBar).toHaveStyle("display: flex");

    const menuItems = screen.getAllByRole("link");
    expect(menuItems.length).toBeGreaterThan(0);
  });

  test("Main banner structure", () => {
    const banner = screen.getByRole("img", { name: /main banner/i });
    expect(banner).toBeInTheDocument();
    expect(banner).toHaveStyle("width: 100%");

    const overlayText = screen.getByText(/event details/i);
    expect(overlayText).toBeInTheDocument();
    expect(overlayText).toHaveStyle("text-align: center");
  });

  test("Content section grid layout", () => {
    const contentSection = screen.getByTestId("content-section");
    expect(contentSection).toHaveStyle(
      "display: grid; grid-template-columns: repeat(4, 1fr)"
    );

    const columns = screen.getAllByTestId(/^column-/);
    columns.forEach((column) => {
      expect(column).toHaveStyle(
        "display: grid; grid-template-columns: repeat(2, 1fr)"
      );
    });
  });

  test("Typography checks", () => {
    const headers = screen.getAllByRole("heading");
    headers.forEach((header) => {
      expect(header).toHaveStyle("font-size: large; font-weight: bold");
    });

    const subTexts = screen.getAllByText(/text/i);
    subTexts.forEach((subText) => {
      expect(subText).toHaveStyle("font-size: medium; font-weight: normal");
    });

    const links = screen.getAllByRole("link");
    links.forEach((link) => {
      expect(link).toHaveStyle("font-size: medium; text-decoration: underline");
    });
  });

  test("Color and styling checks", () => {
    const background = screen.getByRole("main");
    expect(background).toHaveStyle("background-color: white");

    const textElements = screen.getAllByText(/text/i);
    textElements.forEach((text) => {
      expect(text).toHaveStyle("color: black");
    });

    const banner = screen.getByRole("banner");
    expect(banner).toHaveStyle("background-color: blue; color: white");
  });

  test("Image dimensions and styling", () => {
    const images = screen.getAllByRole("img");
    images.forEach((image) => {
      expect(image).toHaveStyle("aspect-ratio: 1 / 1; border-radius: 8px");
    });
  });

  test("Interactive elements", () => {
    const buttons = screen.getAllByRole("button");
    buttons.forEach((button) => {
      expect(button).toHaveStyle("transition: background-color 0.3s");
      button.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      expect(button).toHaveStyle("background-color: darken");
    });

    const links = screen.getAllByRole("link");
    links.forEach((link) => {
      link.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
      expect(link).toHaveStyle("text-decoration: underline");
    });
  });
});
