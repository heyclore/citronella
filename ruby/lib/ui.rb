def ui(args)
  baz = Struct.new(:page, :locator)
  baz.new(args.delete(:page), args)
end
