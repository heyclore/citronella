def ui(args)
  baz = Struct.new(:page, :exception, :locator)
  baz.new(args.delete(:page), args.delete(:exception), args)
end
